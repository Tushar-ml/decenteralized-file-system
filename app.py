from distutils.command.upload import upload
from flask import Flask, render_template,request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import uuid
import datetime
import pandas as pd

app = Flask(__name__)

ROOT_DIR = os.path.dirname(__file__)
file_folder = f'{ROOT_DIR}/files/'

files_dic = []
uplink_config = os.getenv('UPLINK_CONFIG',default='./uplink')
@app.route('/', methods=['GET'])
def file_maintainer():
    name = request.args.get('name') if request.args.get('name') is not None else ''
    size = request.args.get('size') if request.args.get('size') is not None else ''
    link = request.args.get('link') if request.args.get('link') is not None else ''
    fileid = request.args.get('fileid') if request.args.get('name') is not None else ''
    return render_template('index.html',name=name, size=size, link=link, fileid=fileid)

@app.route('/upload',methods=['GET','POST'])
def uploader():
    if request.method == 'POST':
        file_id = uuid.uuid4().hex
        f = request.files['file']
        uploaded_file_path = f'{file_folder}/{secure_filename(f.filename)}'
        f.save(uploaded_file_path)
        
        os.system(f'{uplink_config} cp "{uploaded_file_path}" "sj://anticensorb/{file_id}@{f.filename}"')
        os.system('rm -f response.txt')
        url = os.system(f'{uplink_config} share --url --base-url=https://link.ap1.storjshare.io "sj://anticensorb/{file_id}@{f.filename}" >> response.txt')
        url_file = open('response.txt','rb').readlines()[-1].decode("utf-8")
        url = 'https:'+url_file.split(':')[-1].strip()
        url = url.replace('/s/','/raw/')
        
        file_size = os.stat(uploaded_file_path).st_size
        files_dic.append({
            'file_id':file_id,
            'filename':f.filename,
            'created_at':datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M"),
            'file_size':file_size,
            'link':url
        })
        
        os.system(f'rm -f {uploaded_file_path}')


    return redirect(url_for('.file_maintainer',name=f.filename, size=file_size, link=url, fileid=file_id))

@app.route('/directory',methods=['GET'])
def file_directory():
    try:
        os.system(f'rm -f directory.txt')
        os.system(f'{uplink_config} ls sj://anticensorb >> directory.txt')
        directory = open('directory.txt','rb').readlines()
        directory = [x.decode('utf-8').strip() for x in directory]
        l = []
        for r in directory[1:]:
            x = [x for x in r.split(' ') if x!='']
            a = {
                'Type':x[0],
                'Date':f'{x[1]} {x[2]}',
                'Size':f'{x[3]}',
                'File':f'{" ".join(x[4:])}'
            }
            l.append(a)

        df = pd.DataFrame(l)
        
        df['file_id'] = df['File'].apply(lambda x: x.split('@')[0] if '@' in x else '')
        df['File'] = df['File'].apply(lambda x: x.split('@')[1] if '@' in x else ''.join(x))

        return df.to_html(header="true", table_id="table")
    except:
        df = pd.DataFrame({
            'Type':[],
            'Date':[],
            'Size':[],
            'File':[],
            'file_id':[]
        })

        return df.to_html(header="true",table_id="table")

if __name__ == '__main__':
    app.run()
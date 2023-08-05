import json
import os
import datetime
from unicodedata import name
from urllib import response
import pandas as pd
from jupyter_server.base.handlers import APIHandler
from jupyter_server.utils import url_path_join
import tornado
import label_studio_sdk
from label_studio_sdk import Client
import json

user_config_route="user/user.json"

def get_api(user_config_path):
    if os.path.exists(user_config_path):
        f=open(user_config_path)
        data=json.load(f)
        return data["api_key"]
    else:
        return None

LABEL_STUDIO_URL = 'http://localhost:8080'




# TODO: add error handler

class CheckLSConnectHandler(APIHandler):
    @tornado.web.authenticated
    def get(self):
        # TODO: better error handling
        try:
            API_KEY=get_api(user_config_route)
            ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
            response=ls.check_connection()
            
            if(response["status"]=="UP"):
                self.finish({"status":"UP"})
            else:
                print("down1")
                raise ValueError
        except:
            print("down2")
            raise ValueError



class ProjectCountHandler(APIHandler):
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server
    @tornado.web.authenticated
    def get(self):
        API_KEY=get_api(user_config_route)
        ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
        pjs=ls.get_projects()
        pj_count=len(pjs)
        self.finish(json.dumps({
            "project_count": pj_count
        }))




class ProjectHandler(APIHandler):
    @tornado.web.authenticated
    def get(self):
        API_KEY=get_api(user_config_route)
        ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
        projects=ls.get_projects()
        names=[i.get_params()["title"] for i in projects]
        ids=[i.id for i in projects]
        list_json=dict(zip(ids,names))
        self.finish(json.dumps(list_json,indent=2,ensure_ascii=False))

    @tornado.web.authenticated
    def post(self):
        API_KEY=get_api(user_config_route)
        ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
        input_data = self.get_json_body()
        proj_name=input_data["name"]
        proj_description=input_data["description"]
        config=input_data['config']
        project=ls.start_project(title=proj_name,label_config=config,description=proj_description)
        id=project.id
        self.finish(json.dumps({
            "id":id
        }))

class ChosenProjectHandler(APIHandler):
    @tornado.web.authenticated
    def post(self):
        API_KEY=get_api(user_config_route)
        input_data = self.get_json_body()
        proj_id=input_data["project_id"]
        ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
        project=ls.get_project(proj_id)
        view=project.get_params()["label_config"]
        tasks=project.get_tasks()


        self.finish(json.dumps({
            "id": proj_id,
            "current_view": view,
            "current_tasks": tasks
        }))


class ExportHandler(APIHandler):
    @tornado.web.authenticated
    def post(self):
        API_KEY=get_api(user_config_route)
        input_data=self.get_json_body()
        proj_id=input_data["project_id"]
        export_format=input_data["format"]
        ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
        proj=ls.get_project(proj_id)
        name=proj.get_params()["title"]

        e=datetime.datetime.now()
        time_str=e.strftime("%Y_%m_%d_%H:%M:%S")

        if(export_format=="JSON"):
            tasks=proj.export_tasks(export_type=export_format)
            # tasks_json=json.dumps(tasks,indent=2)
            output_name="{}_{}.json".format(name,time_str)
            with open(output_name,mode="w",encoding="utf-8") as f:
                json.dump(tasks,f,indent=4)


            self.finish({
                "response":200

            })

        elif(export_format=="CSV"):

            from io import StringIO
            response = ls.make_request(
                method='GET',
                url=f'/api/projects/{proj_id}/export?exportType=CSV'
            )
            export_byte=response.content
            export_csv=pd.read_csv(StringIO(export_byte.decode()))
            export_csv.to_csv("{}_{}.csv".format(name,time_str))

            self.finish({
                "response":200,
            })






class CreateProjectHandler(APIHandler):
    @tornado.web.authenticated
    def post(self):
        API_KEY=get_api(user_config_route)
        ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
        input_data=self.get_json_body()
        name=input_data["project_name"];
        description=input_data["description"];
        label_config=input_data["label_config"];
        ls.start_project(title=name,
                        description=description,
                        label_config=label_config)
        self.finish({"response":200})


class ConnectLocalStorageHandler(APIHandler):
    @tornado.web.authenticated
    def post(self):
        API_KEY=get_api(user_config_route)
        ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
        input_data=self.get_json_body()
        #TODO: follow the repo issue here: https://github.com/heartexlabs/label-studio-sdk/issues/59
        #TODO: add an sync_storage from client at the end
        project_id=input_data["project_id"]
        local_name=input_data["storage_name"]
        regex=input_data["regex"]
        local_path=input_data["path"]

        payload={
            'regex_filter': regex,
            'path': local_path,
            'title': local_name,
            'project': project_id,
            'use_blob_urls': True,
        }

        response=ls.make_request('POST', f'/api/storages/localfiles', json=payload)
        if response.status_code==201:
            localfiles=response.json()
            current_storage=ls.make_request('GET',f'/api/storages/?project={project_id}')
            storage_id=localfiles["id"]
            # sync_response=ls.make_request('POST', f'/api/storages/localfiles/{storage_id}/sync', json=payload)
            ls.sync_storage(storage_type="localfiles",storage_id=storage_id)

            self.finish({
                "response":201,
                "id":project_id,
                "storage_list":current_storage.json()
            })




class CheckConnectionHandler(APIHandler):
    @tornado.web.authenticated
    def post(self):
        API_KEY=get_api(user_config_route)
        ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
        input_data=self.get_json_body()
        project_id=input_data["project_id"]
        local_name=input_data["storage_name"]
        regex=input_data["regex"]
        local_path=input_data["path"]
        # print(os.environ[LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED])
        # print(os.environ[LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT])

        payload={
            'regex_filter': regex,
            'use_blob_urls': True,
            'path': local_path,
            'last_sync': "2019-08-24T14:15:22Z",
            'last_sync_count': 0,
            'title': local_name,
            'description': "",
            'project': project_id
        }

        response=ls.make_request('POST', f'/api/storages/localfiles/validate', json=payload)
        if response.status_code == 200:
            self.finish({
                "response":200
            })

# class ConnectGoogleCloudStorageHandler(APIHandler):
#     @tornado.web.authenticated
#     def post(self):
#         ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
#         input_data=self.get_json_body()

class SyncStorageHandler(APIHandler):
    @tornado.web.authenticated
    def post(self):
        API_KEY=get_api(user_config_route)
        input_data=self.get_json_body()
        ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
        storage_id=input_data["storage_id"]
        storage_type=input_data["storage_type"]
        reply=ls.sync_storage(storage_type=storage_type,storage_id=storage_id)
        self.finish(json.dumps(reply))










# TODO: set next three handler into one
class UpdateTaskAnnotationHandler(APIHandler):
    @tornado.web.authenticated
    def post(self):
        API_KEY=get_api(user_config_route)
        ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
        input_data=self.get_json_body()
        proj_id=input_data["project_id"]
        task_id=input_data["task_id"]
        anno_id=input_data["annotation_id"]
        payload=input_data["annotation_result"]
        proj=ls.get_project(proj_id)
        proj.update_annotation(annotation_id=anno_id,result=payload)

        task=proj.get_task(task_id)
        self.finish({
            "updated_task":task
        })

class DeleteTaskAnnotationHandler(APIHandler):
    @tornado.web.authenticated
    def post(self):
        API_KEY=get_api(user_config_route)
        ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
        input_data=self.get_json_body()
        proj_id=input_data["project_id"]
        task_id=input_data["task_id"]
        anno_id=input_data["annotation_id"]
        response=ls.make_request('DELETE', f'/api/annotations/{anno_id}')
        if response.status_code==204:
            proj=ls.get_project(proj_id)
            task=proj.get_task(task_id)
            self.finish({
                "updated_task":task
            })


class SubmitTaskAnnotationHandler(APIHandler):
    @tornado.web.authenticated
    def post(self):
        API_KEY=get_api(user_config_route)
        ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
        input_data=self.get_json_body()
        proj_id=input_data["project_id"]
        task_id=input_data["task_id"]
        result=input_data["annotation_result"]
        payload={
            "result":result,
            "task":task_id,
        }
        response=ls.make_request('POST', f'/api/tasks/{task_id}/annotations', json=payload)
        # print(response)
        if response.status_code==201:
            project=ls.get_project(proj_id)
            task=project.get_task(task_id)
            self.finish({
                "updated_task":task
            })




class GeneralStorageHandler(APIHandler):
    @tornado.web.authenticated
    def post(self):
        API_KEY=get_api(user_config_route)
        ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
        input_data=self.get_json_body()
        proj_id=input_data["project_id"]
        reply=ls.make_request('GET',f'/api/storages/?project={proj_id}')
        if reply.status_code==200:
            self.finish({
                "id":proj_id,
                "storage_list":reply.json()
            })





def setup_handlers(web_app):
    host_pattern = ".*$"




    base_url = web_app.settings["base_url"]
    count_pattern = url_path_join(base_url, "jupyter-labelstudio-extension", "count")
    projects_pattern = url_path_join(base_url, "jupyter-labelstudio-extension", "projects")
    chosen_project_pattern = url_path_join(base_url, "jupyter-labelstudio-extension", "current")
    export_pattern=url_path_join(base_url, "jupyter-labelstudio-extension", "export")
    validate_pattern=url_path_join(base_url, "jupyter-labelstudio-extension", "validate")
    update_pattern=url_path_join(base_url, "jupyter-labelstudio-extension", "update")
    submit_pattern=url_path_join(base_url, "jupyter-labelstudio-extension", "submit")
    delete_pattern=url_path_join(base_url, "jupyter-labelstudio-extension", "delete")
    sync_pattern=url_path_join(base_url, "jupyter-labelstudio-extension", "sync")
    connect_ls_pattern=url_path_join(base_url, "jupyter-labelstudio-extension", "connect")
    connect_local_pattern=url_path_join(base_url, "jupyter-labelstudio-extension", "connect","local")
    storage_pattern=url_path_join(base_url, "jupyter-labelstudio-extension","storage")

    handlers = [(connect_ls_pattern, CheckLSConnectHandler),
                (count_pattern, ProjectCountHandler),
                (projects_pattern,ProjectHandler),
                (chosen_project_pattern, ChosenProjectHandler),
                (export_pattern, ExportHandler),
                (validate_pattern,CheckConnectionHandler),
                (storage_pattern,GeneralStorageHandler),
                (update_pattern,UpdateTaskAnnotationHandler),
                (submit_pattern,SubmitTaskAnnotationHandler),
                (delete_pattern,DeleteTaskAnnotationHandler),
                (connect_local_pattern,ConnectLocalStorageHandler),
                (sync_pattern,SyncStorageHandler)]
    web_app.add_handlers(host_pattern, handlers)

import ProjectPanel from './components/project';
import ExportPanel from './export';
import LabelStudio from 'label-studio';
import 'label-studio/build/static/css/main.css';

import React, { useEffect, useState } from 'react';
import { Button } from '@material-ui/core';
import { requestAPI } from './handler';

// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
const ProjectUI = () => {
  const [currentID, setID] = useState(-1);
  const [tasks, setTasks] = useState([{}]);
  // const [currentTask, setCurrentTask] = useState({});
  const [currentIndex, setCurrentIndex] = useState(0);
  const [currentConfig, setCurrentConfig] = useState('');
  const [currentPanel, setCurrentPanel] = useState({
    config: '',
    task: {}
  });

  const onClickPrevMission = () => {
    if (currentIndex > 0) {
      setCurrentPanel({
        config: currentConfig,
        task: tasks[currentIndex - 1]
      });
      setCurrentIndex(currentIndex - 1);
    }
  };
  const onClickNextMission = () => {
    if (currentIndex < tasks.length - 1) {
      setCurrentPanel({
        config: currentConfig,
        task: tasks[currentIndex + 1]
      });
      setCurrentIndex(currentIndex + 1);
    }
  };

  const updateCurrentPanel = (data: any) => {
    //TODO: fixed URL(changes to default URL)
    //TODO: change data type to json object
    const tasks_raw = data['current_tasks'];
    for (let i = 0; i < tasks_raw.length; i++) {
      const image_path = tasks_raw[i]['data']['image'];
      const base_url = 'http://localhost:8080';
      tasks_raw[i]['data']['image'] = base_url + image_path;
    }
    setTasks(tasks_raw);
    setCurrentConfig(data['current_view']);
    setCurrentPanel({
      config: data['current_view'],
      task: tasks_raw[0]
    });
    setCurrentIndex(0);
    //TODO: error handle
    setID(data['id']);
    // console.log('current task: ', tasks_raw[0]);
    // console.log('current config: ', currentConfig);
  };

  const updateCurrentTask = (task: any, base_url: string) => {
    const image_path = task['data']['image'];
    task['data']['image'] = base_url + image_path;

    const new_tasks = [...tasks];
    new_tasks[currentIndex] = task;
    setTasks(new_tasks);
    setCurrentPanel({
      config: currentConfig,
      task: task
    });
  };

  useEffect(() => {
    if (currentID >= 0) {
      new LabelStudio('label-studio', {
        config: currentPanel.config,
        interfaces: [
          'panel',
          'update',
          'submit',
          'controls',
          'infobar',
          'topbar',
          'instruction',
          'side-column',
          'annotations:history',
          'annotations:tabs',
          'annotations:menu',
          'annotations:current',
          'annotations:add-new',
          'annotations:delete',
          'annotations:view-all',
          'edit-history'
        ],

        user: {
          pk: 1,
          firstName: 'Test',
          lastName: 'Account'
        },
        task: currentPanel.task,
        //TODO: any type modification
        onLabelStudioLoad: function (LS: any) {
          const c = LS.annotationStore.addAnnotation({
            userGenerate: true
          });
          LS.annotationStore.selectAnnotation(c.id);
        },

        onSubmitAnnotation: async function (LS: any, annotation: any) {
          // eslint-disable-next-line @typescript-eslint/ban-ts-comment
          // @ts-ignore
          //TODO: change it to better
          const id = currentPanel.task['id'];
          // const annotation = annotation.serializeAnnotation();
          try {
            const reply = await requestAPI<any>('submit', {
              body: JSON.stringify({
                project_id: currentID,
                task_id: id,
                annotation_result: annotation.serializeAnnotation()
              }),
              method: 'POST'
            });

            const update_task = reply['updated_task'];
            updateCurrentTask(update_task, 'http://localhost:8080');
          } catch (reason) {
            console.error(
              `Error on POST /jupyterlab_labelstudio_extension/submit.\n${reason}`
            );
          }
        },

        onUpdateAnnotation: async function (LS: any, annotation: any) {
          // eslint-disable-next-line @typescript-eslint/ban-ts-comment
          // @ts-ignore
          //TODO: change it to better
          const task_id = currentPanel.task['id'];
          const annotation_id = annotation.pk;
          const annotation_result = annotation.serializeAnnotation();

          try {
            const reply = await requestAPI<any>('update', {
              body: JSON.stringify({
                project_id: currentID,
                task_id: task_id,
                annotation_id: annotation_id,
                annotation_result: annotation_result
              }),
              method: 'POST'
            });

            const update_task = reply['updated_task'];
            updateCurrentTask(update_task, 'http://localhost:8080');
          } catch (reason) {
            console.error(
              `Error on POST /jupyterlab_labelstudio_extension/update.\n${reason}`
            );
          }
        },

        onDeleteAnnotation: async function (LS: any, annotation: any) {
          // eslint-disable-next-line @typescript-eslint/ban-ts-comment
          // @ts-ignore
          //TODO: change it to better
          const task_id = currentPanel.task['id'];
          const annotation_id = annotation.pk;

          //TODO: delete post
          try {
            const reply = await requestAPI<any>('delete', {
              body: JSON.stringify({
                project_id: currentID,
                task_id: task_id,
                annotation_id: annotation_id
              }),
              method: 'POST'
            });

            const update_task = reply['updated_task'];
            updateCurrentTask(update_task, 'http://localhost:8080');
          } catch (reason) {
            console.error(
              `Error on POST /jupyterlab_labelstudio_extension/delete.\n${reason}`
            );
          }
        }
      });
    }
  }, [currentPanel, currentID]);

  //TODO: potential bug test for boundary tasks
  return (
    <div>
      <h2 style={{ marginLeft: '2%' }}>Choose Project</h2>
      <ProjectPanel type="labeling" updateFunc={updateCurrentPanel} />
      <div id="project-content" style={{ display: 'none' }}>
        <h2 style={{ marginLeft: '2%' }}>Labeling</h2>
        <Button
          variant="contained"
          style={{ color: 'white', backgroundColor: '#448ef7', margin: '4%' }}
          onClick={onClickPrevMission}
          disabled={currentIndex === 0}
        >
          Last
        </Button>
        <Button
          variant="contained"
          style={{ color: 'white', backgroundColor: '#448ef7', margin: '4%' }}
          onClick={onClickNextMission}
          disabled={currentIndex === tasks.length - 1}
        >
          Next
        </Button>
        <br />
        {currentID >= 0 && <div id="label-studio"> </div>}
        <h2 style={{ marginLeft: '2%' }}>Export</h2>
        {currentID >= 0 && <ExportPanel projectID={currentID} />}
      </div>
    </div>
  );
};

export default ProjectUI;

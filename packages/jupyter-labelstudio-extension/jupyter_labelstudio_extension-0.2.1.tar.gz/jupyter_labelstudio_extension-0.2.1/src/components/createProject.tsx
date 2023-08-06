import { Button, TextField } from '@material-ui/core';
import React, { useEffect, useState } from 'react';
import { requestAPI } from '../handler';

// eslint-disable-next-line @typescript-eslint/naming-convention
interface CreateProjectProps {
  template?: string;
  updateFunc?: (data: number) => void;
}

// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types,@typescript-eslint/ban-ts-comment
// @ts-ignore
export const CreateProjectInput = ({
  template,
  updateFunc
}: CreateProjectProps) => {
  const [nameValue, setNameValue] = useState('');
  const [description, setDescription] = useState('');

  const onNameChange = (e: any) => setNameValue(e.target.value);
  const onDescriptionChange = (e: any) => setDescription(e.target.value);

  useEffect(() => {
    requestAPI('count')
      .then((data: any) => {
        const num = data['project_count'] + 1;
        setNameValue('New Project #' + num.toString());
      })
      .catch(reason => {
        console.error(
          `The jupyter_labelstudio_extension server extension appears to be missing.\n${reason}`
        );
      });
  }, []);

  async function handleCreate() {
    try {
      const reply = await requestAPI<any>('projects', {
        body: JSON.stringify({
          name: nameValue,
          config: template,
          description: description
        }),
        method: 'POST'
      });

      if (updateFunc) {
        updateFunc(reply['id']);
      }
      // eslint-disable-next-line @typescript-eslint/ban-ts-comment
      // @ts-ignore
      document.getElementById('create-project-button').style.display = 'none';
      alert('Successfully create project.');
    } catch (reason) {
      console.error(
        `Error on POST /jupyterlab_labelstudio_extension/projects.\n${reason}`
      );
      alert('failed to create project.');
    }
  }

  return (
    <div>
      <TextField
        id="proj_name"
        label="Project Name"
        variant="outlined"
        value={nameValue}
        onChange={onNameChange}
        required
      />
      <br />
      <TextField
        id="proj_description"
        label="Project Description"
        value={description}
        variant="outlined"
        onChange={onDescriptionChange}
      />
      <br />
      <Button
        id="create-project-button"
        style={{ backgroundColor: '#448ef7', color: 'white', marginTop: '2%' }}
        onClick={handleCreate}
      >
        Create Project
      </Button>
    </div>
  );
};

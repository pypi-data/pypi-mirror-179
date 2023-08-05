import React, { useEffect, useState } from 'react';
// import { config } from 'webpack';

import { requestAPI } from '../handler';

// eslint-disable-next-line @typescript-eslint/naming-convention
interface ProjectPanelProps {
  type?: string;
  updateFunc?: (data: any) => void;
}

// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
export const ProjectPanel = ({ type, updateFunc }: ProjectPanelProps) => {
  const [projectNames, setProjectNames] = useState([]);
  const [projectIDs, setProjectIDs] = useState([]);
  const [isEmpty, setEmpty] = useState(false);

  async function handleCheckProject(projectId: any) {

    try {
      if (type === 'labeling') {
        const reply = await requestAPI<any>('current', {
          body: JSON.stringify({ project_id: projectId }),
          method: 'POST'
        });

        if (updateFunc) {
          updateFunc(reply);
        }

        // eslint-disable-next-line @typescript-eslint/ban-ts-comment
        // @ts-ignore
        document.getElementById('project-content').style.display = 'block';
      }
      if (type === 'storage') {

        const reply = await requestAPI<any>('storage', {
          body: JSON.stringify({ project_id: projectId }),
          method: 'POST'
        });

        console.log(reply);
        if (updateFunc) {
          updateFunc(reply);
        }
        //
        // // eslint-disable-next-line @typescript-eslint/ban-ts-comment
        // // @ts-ignore
        // document.getElementById('storage-list').style.display = 'block';
      }
    } catch (reason) {
      console.error(`Error on ProjectPanel rendering.\n${reason}`);
    }
  }

  useEffect(() => {
    requestAPI<any>('projects')
      .then(data => {
        // TODO: ignore ts compile, fix this when available
        // eslint-disable-next-line @typescript-eslint/ban-ts-comment
        // @ts-ignore
        setProjectIDs(Object.keys(data));
        setProjectNames(Object.values(data));
        if (Object.keys(data).length === 0) {
          setEmpty(true);
        }
      })
      .catch(reason => {
        console.error(
          `The jupyter_labelstudio_extension server extension appears to be missing.\n${reason}`
        );
      });
  }, []);

  // TODO: beautify frontend
  return (
    <div>
      {isEmpty && (
        <p style={{ marginLeft: '2%' }}>
          {' '}
          You don't have any project now. Please go to "create project" to
          create one{' '}
        </p>
      )}
      {!isEmpty && (
        <div
          style={{
            display: 'flex',
            overflowX: 'scroll',
            width: '95%',
            marginLeft: '2%',
            cursor: 'pointer'
          }}
        >
          {projectNames.map((src, index) => (
            <div
              key={projectIDs[index]}
              style={{
                width: '300px',
                height: '200px',
                borderRadius: '10px',
                borderStyle: 'solid',
                borderColor: 'black',
                marginLeft: '10px'
              }}
              onClick={() => handleCheckProject(projectIDs[index])}
            >
              Name: {src}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default ProjectPanel;

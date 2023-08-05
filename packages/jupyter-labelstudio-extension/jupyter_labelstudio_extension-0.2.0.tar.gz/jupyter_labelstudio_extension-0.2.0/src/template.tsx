// import { ReactWidget } from "@jupyterlab/apputils";
// import LabelStudio from "label-studio"
import 'label-studio/build/static/css/main.css';
import { ViewUpdate } from '@codemirror/view';
import CodeMirror from '@uiw/react-codemirror';
// from :https://github.com/uiwjs/react-codemirror
import React, { useEffect, useState } from 'react';
import { html } from '@codemirror/lang-html';
import LabelStudio from 'label-studio';
import 'label-studio/build/static/css/main.css';

import { StorageTabs } from './components/storageTabs';
import { CreateProjectInput } from './components/createProject';

// eslint-disable-next-line @typescript-eslint/naming-convention
interface TemplateProps {
  config: string;
}

//BUGS TODO:!! empty error
const TemplatePreview = (props: TemplateProps) => {
  const { config } = props;
  // const [renderError,setRenderError]=useState(false);

  // let templateImgURL= "./assets/template.jpg"

  //TODO：Setting States
  useEffect(() => {
    try {
      new LabelStudio('template-preview', {
        config: config,

        interfaces: ['update', 'controls'],

        user: {
          pk: 1,
          firstName: 'James',
          lastName: 'Dean'
        },
        task: {
          annotations: [],
          predictions: [],
          id: 1,
          data: {
            image:
              'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.eduwo.com%2Fu%2Fcms%2Fwww%2F201503%2F11151325i4p2.jpg&refer=http%3A%2F%2Fwww.eduwo.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1668566302&t=ce01be687029ada4e4694c44cdb2d34b'
          }
        },
        onLabelStudioLoad: function (LS: any) {
          const c = LS.annotationStore.addAnnotation({
            userGenerate: true
          });
          LS.annotationStore.selectAnnotation(c.id);
        }
      });
    } catch (reason) {
      console.error(`Error on rendering with current config.\n${reason}`);
    }
  });

  return (
    <div
      style={{ flex: '1', width: '45%', height: '500px' }}
      id="template-preview"
    />
  );
};

export default TemplatePreview;

// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
export function TemplateUI() {
  // TODO: add react config
  const default_code = `<View>
  <Image name="image" value="$image"/>
  <Choices name="choice" toName="image" showInLine="true">
    <Choice value="Boeing"/>
    <Choice value="Airbus"/>
  </Choices>
</View>
    `;

  const [currentCode, setCode] = useState(default_code);
  const [currentProject, setCurrentProject] = useState(-1);

  const onChange = React.useCallback(
    (value: string, viewUpdate: ViewUpdate) => {
      setCode(value);
    },
    []
  );

  function onClickImageClassification() {
    setCode(`<View>
  <Image name="image" value="$image"/>
  <Choices name="choice" toName="image" showInLine="true">
    <Choice value="Boeing"/>
    <Choice value="Airbus"/>
  </Choices>
</View>
    `);
  }

  function onClickObjectDetection() {
    setCode(`<View>
  <Image name="image" value="$image"/>
  <RectangleLabels name="label" toName="image">
    <Label value="Airplane" background="green"/>
    <Label value="Car" background="blue"/>
  </RectangleLabels>
</View>

    `);
  }

  return (
    <div>
      <h1 style={{ marginLeft: '2%' }}>Label Studio Interface</h1>
      <h2 style={{ marginLeft: '2%' }}>Choose Tasks</h2>
      <div style={{ marginLeft: '2%' }}>
        <button style={{ margin: '1%' }} onClick={onClickImageClassification}>
          Image Classification
        </button>
        <button style={{ margin: '1%' }} onClick={onClickObjectDetection}>
          Object Detection
        </button>
      </div>
      <h2 style={{ marginLeft: '2%' }}>Labeling Template</h2>
      <div
        style={{
          display: 'flex',
          marginLeft: '2%',
          width: '95%',
          marginBottom: '1em'
        }}
      >
        <CodeMirror
          value={currentCode}
          height="500px"
          style={{ width: '50%', fontSize: '20' }}
          onChange={onChange}
          extensions={[html()]}
        />
        <TemplatePreview config={currentCode} />
      </div>
      <h2 style={{ marginLeft: '2%' }}>Create Project</h2>
      <div style={{ marginLeft: '2%' }}>
        <CreateProjectInput
          template={currentCode}
          updateFunc={(data: number) => {
            setCurrentProject(data);
          }}
        />
      </div>
      <h2 style={{ marginLeft: '2%' }}>Link with Local Storage/Google Cloud</h2>
      <div style={{ marginLeft: '2%' }}>
        {currentProject >= 0 && <StorageTabs projectID={currentProject} />}
      </div>
    </div>
  );
}

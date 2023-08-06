import { ReactWidget } from '@jupyterlab/apputils';

import 'label-studio/build/static/css/main.css';
import InstructionPage from './instruction';

import React, { useEffect, useState } from 'react';
// import {Route} from "react-router-dom"
// import {useNavigate} from "react-router"
import { TemplateUI } from './template';
import ProjectUI from './labelProject';
import { StorageUI } from './storageManagement';
import { Button } from '@material-ui/core';
import { AppBar } from '@material-ui/core';
import { Toolbar } from '@material-ui/core';
import { requestAPI } from './handler';

// Single label
function LabelStudioUI() {
  const [page, setPage] = useState('create');

  const onClickCreate = () => {
    setPage('create');
  };

  const onClickLabel = () => {
    setPage('label');
  };

  const onClickStorage = () => {
    setPage('storage');
  };

  const showCreateProjectUI = () => {
    if (page === 'create') {
      return <TemplateUI />;
    }
  };

  const showLabelingProjectUI = () => {
    if (page === 'label') {
      return <ProjectUI />;
    }
  };

  const showStorageUI = () => {
    if (page === 'storage') {
      return <StorageUI />;
    }
  };

  return (
    <div>
      <div style={{ flexGrow: 1 }}>
        {/*<AppBar position="static" color="transparent">*/}
        <AppBar position="static" style={{ backgroundColor: '#448ef7' }}>
          <Toolbar>
            <Button style={{ color: 'white' }} onClick={onClickCreate}>
              {' '}
              Create Project
            </Button>
            <Button style={{ color: 'white' }} onClick={onClickLabel}>
              {' '}
              Label Project
            </Button>
            <Button style={{ color: 'white' }} onClick={onClickStorage}>
              {' '}
              Storage Management
            </Button>
          </Toolbar>
        </AppBar>
      </div>

      {showCreateProjectUI()}
      {showLabelingProjectUI()}
      {showStorageUI()}
    </div>
  );
}

const LabelStudioComponent = (): JSX.Element => {
  const [connected, setConnected] = useState(false);

  useEffect(() => {
    requestAPI('connect')
      .then((data: any) => {
        if (data['status'] === 'UP') {
          console.log('status is up');
          setConnected(true);
        } else {
          console.log('status is down');
          setConnected(false);
        }
      })
      .catch(reason => {
        console.log('status error');
        setConnected(false);
      });
  }, []);

  return <div>{connected ? <LabelStudioUI /> : <InstructionPage />}</div>;
};

export class LabelStudioWidget extends ReactWidget {
  constructor() {
    super();
    this.addClass('jp-LabelStudioWidget');
  }
  render(): JSX.Element {
    return (
      <div style={{ height: '100%', width: '100%', overflow: 'scroll' }}>
        <LabelStudioComponent />
      </div>
    );
  }
}

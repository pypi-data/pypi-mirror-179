import { Button, Tabs, TextField } from '@material-ui/core';
import { Tab } from '@material-ui/core';
import * as React from 'react';
import { Box } from '@material-ui/core';
import { Typography } from '@material-ui/core';
import { useState } from 'react';
import { requestAPI } from '../handler';

// eslint-disable-next-line @typescript-eslint/naming-convention
interface TabPanelProps {
  children?: React.ReactNode;
  index: number;
  value: number;
}

function TabPanel(props: TabPanelProps) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: 3 }}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}

function a11yProps(index: number) {
  return {
    id: `simple-tab-${index}`,
    'aria-controls': `simple-tabpanel-${index}`
  };
}

// eslint-disable-next-line @typescript-eslint/naming-convention
interface StorageTabProps {
  projectID?: number;
  updateFunc?: (data: any) => void;
}

// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
export const StorageTabs = ({ projectID, updateFunc }: StorageTabProps) => {
  const [localName, setLocalName] = useState('');
  const [localPath, setLocalPath] = useState('');
  //TODO: change regex according to tasks type
  const [regex, setRegex] = useState('.*(jpe?g|png)');
  const [value, setValue] = React.useState(0);

  async function handleCheckConnection() {
    console.log(projectID);
    console.log(localName);
    console.log(regex);
    console.log(localPath);
    try {
      const reply = await requestAPI<any>('validate', {
        body: JSON.stringify({
          project_id: projectID,
          storage_name: localName,
          path: localPath,
          regex: regex
        }),
        method: 'POST'
      });
      console.log(reply);
      alert(
        'Connection clear. You can click "add storage" to connect the storage.'
      );
    } catch (reason) {
      console.error(
        `Error on POST /jupyterlab_labelstudio_extension/export.\n${reason}`
      );
      alert(
        'Connection failed. Check if the absolute path and regex is correct, or if the local config is set.'
      );
    }
  }

  async function handleAddLocalStorage() {
    try {
      const reply = await requestAPI<any>('connect/local', {
        body: JSON.stringify({
          project_id: projectID,
          storage_name: localName,
          path: localPath,
          regex: regex
        }),
        method: 'POST'
      });
      console.log('reply:', reply);
      alert('Successfully create and sync local storage');
      console.log(updateFunc);
      if (updateFunc) {
        updateFunc(reply);
      }
    } catch (reason) {
      console.error(
        `Error on POST /jupyterlab_labelstudio_extension/connect/local.\n${reason}`
      );
      alert(
        'Fail to create. Check if the absolute path and regex is correct, or if the local config is set.'
      );
    }
  }

  // eslint-disable-next-line @typescript-eslint/ban-types
  const handleChange = (event: React.ChangeEvent<{}>, newValue: number) => {
    setValue(newValue);
  };

  const handleLocalNameChange = (e: any) => setLocalName(e.target.value);
  const handleLocalPathChange = (e: any) => setLocalPath(e.target.value);
  const handleRegexChange = (e: any) => setRegex(e.target.value);

  return (
    <Box sx={{ width: '100%' }}>
      <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
        <Tabs
          value={value}
          onChange={handleChange}
          aria-label="basic tabs example"
          centered
        >
          <Tab label="Local" {...a11yProps(0)} />
          <Tab label="Google Cloud" {...a11yProps(1)} />
        </Tabs>
      </Box>
      <TabPanel value={value} index={0}>
        <TextField
          style={{ margin: '1%' }}
          id="local_storage_title"
          label="Storage Title:"
          value={localName}
          onChange={handleLocalNameChange}
          variant="outlined"
        />
        <TextField
          style={{ margin: '1%' }}
          id="local_path"
          label="Absolute Path"
          value={localPath}
          onChange={handleLocalPathChange}
          variant="outlined"
          required
        />
        <TextField
          style={{ margin: '1%' }}
          id="local_regex"
          label="File Filter Regex"
          value={regex}
          onChange={handleRegexChange}
          variant="outlined"
        />
        <br />
        <Button
          variant="contained"
          style={{ backgroundColor: '#448ef7', color: 'white', margin: '4%' }}
          onClick={handleCheckConnection}
        >
          Check Connection
        </Button>
        <Button
          variant="contained"
          style={{ backgroundColor: '#448ef7', color: 'white', margin: '4%' }}
          onClick={handleAddLocalStorage}
        >
          Add Storage
        </Button>
      </TabPanel>
      {/*TODO: add google cloud state*/}
      <TabPanel value={value} index={1}>
        <TextField
          style={{ margin: '1%' }}
          id="gc_storage_title"
          label="Storage Title:"
          variant="outlined"
        />
        <TextField
          style={{ margin: '1%' }}
          id="gc_bucket_name"
          label="Bucket Name"
          variant="outlined"
          required
        />
        <br />
        <TextField
          style={{ margin: '1%' }}
          id="gc_regex"
          label="File Filter Regex"
          variant="outlined"
          required
        />
        {/*TODO: change credentials display to password*/}
        <TextField
          style={{ margin: '1%' }}
          id="gc_credentials"
          label="Google Application Credentials"
          variant="outlined"
        />
        <br />
        {/*<Button onClick={handleCheckConnection}>Check Connection</Button>*/}
        {/*<Button>Add Storage</Button>*/}
      </TabPanel>
      {/*<TabPanel value={value} index={2}>*/}
      {/*  <TextField*/}
      {/*    id="gc_storage_title"*/}
      {/*    label="Storage Title:"*/}
      {/*    variant="outlined"*/}
      {/*  />*/}
      {/*  <TextField*/}
      {/*    id="gc_bucket_name"*/}
      {/*    label="Bucket Name"*/}
      {/*    variant="outlined"*/}
      {/*    required*/}
      {/*  />*/}
      {/*  <br />*/}
      {/*  <TextField*/}
      {/*    id="gc_regex"*/}
      {/*    label="File Filter Regex"*/}
      {/*    variant="outlined"*/}
      {/*    required*/}
      {/*  />*/}
      {/*  /!*TODO: change credentials display to password*!/*/}
      {/*  <TextField*/}
      {/*    id="gc_credentials"*/}
      {/*    label="Google Application Credentials"*/}
      {/*    variant="outlined"*/}
      {/*  />*/}
      {/*  <br />*/}
      {/*  <Button onClick={handleCheckConnection}>Check Connection</Button>*/}
      {/*  <Button>Add Storage</Button>*/}
      {/*</TabPanel>*/}
    </Box>
  );
};

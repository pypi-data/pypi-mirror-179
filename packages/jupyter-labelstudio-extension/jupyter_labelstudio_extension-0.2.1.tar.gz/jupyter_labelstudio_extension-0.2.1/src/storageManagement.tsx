import React, { useState } from 'react';
import ProjectPanel from './components/project';
// import { StorageCard } from './components/storageCard';
import { Button, DialogActions, DialogContent } from '@material-ui/core';
import { StorageCard } from './components/storageCard';
import { Dialog } from '@material-ui/core';
import { DialogTitle } from '@material-ui/core';
import { StorageTabs } from './components/storageTabs';

export const StorageUI = () => {
  const [currentID, setID] = useState(-1);
  const [storageList, setStorageList] = useState([
    {
      id: undefined,
      path: undefined,
      type: undefined
    }
  ]);
  const [dialogOpen, setDialogOpen] = useState(false);

  const handleOpenDialog = () => {
    setDialogOpen(true);
  };

  const handleClose = () => {
    setDialogOpen(false);
  };

  const updateCurrentPanel = (data: any) => {
    console.log('data:', data);
    setID(data['id']);
    setStorageList(data['storage_list']);
    handleClose();
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-ignore
    document.getElementById('storage-list').style.display = 'block';
  };

  return (
    <div>
      <h2 style={{ marginLeft: '2%' }}>Choose Project</h2>
      <ProjectPanel type="storage" updateFunc={updateCurrentPanel} />
      <div id="storage-list" style={{ display: 'none', marginLeft: '2%' }}>
        <h2>Storage List</h2>
        <Button
          variant="contained"
          style={{ backgroundColor: '#448ef7', color: 'white', margin: '4%' }}
          onClick={handleOpenDialog}
        >
          add storage
        </Button>
        <Dialog open={dialogOpen} onClose={handleClose}>
          <DialogTitle>Link with cloud storage</DialogTitle>
          <DialogContent>
            <StorageTabs
              projectID={currentID}
              updateFunc={updateCurrentPanel}
            />
          </DialogContent>
          <DialogActions>
            <Button onClick={handleClose}>Close</Button>
          </DialogActions>
        </Dialog>

        {storageList.length === 0 && (
          <p> there's no storage for this project, u can try to create one </p>
        )}
        {storageList.map((src, index) => (
          <div>
            <StorageCard
              storageID={src['id']}
              storagePath={src['path']}
              storageType={src['type']}
            />
          </div>
        ))}
      </div>
    </div>
  );
};

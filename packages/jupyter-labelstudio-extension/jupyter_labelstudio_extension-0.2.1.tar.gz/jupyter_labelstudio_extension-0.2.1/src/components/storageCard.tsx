import React from 'react';
import { Card } from '@material-ui/core';
import { Typography } from '@material-ui/core';
// import { CardContent } from '@material-ui/core';
// import { CardActions } from '@material-ui/core';
import { Button } from '@material-ui/core';
import { requestAPI } from '../handler';
import { Container } from '@material-ui/core';

// eslint-disable-next-line @typescript-eslint/naming-convention
interface StorageProps {
  storageID?: number;
  storageType?: string;
  storagePath?: string;
}

export const StorageCard = ({
  storageID,
  storageType,
  storagePath
}: StorageProps) => {
  //TODO: add more color set for s3 and google drive
  // const colorSet = {
  //   localfiles: '#47cf73'
  // };

  async function handleSyncStorage() {
    try {
      await requestAPI<any>('sync', {
        body: JSON.stringify({
          storage_id: storageID,
          storage_type: storageType
        }),
        method: 'POST'
      });
      alert('successfully sync storage at ' + storageType);
    } catch (reason) {
      console.error(
        `Error on POST /jupyterlab_labelstudio_extension/sync.\n${reason}`
      );
      //TODO: specific error tip
      alert('Sync error');
    }
  }

  return (
    <Container
      style={{
        width: '30%',
        margin: '2%',
        padding: '2%',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        flexWrap: 'wrap',
        overflow: 'auto'
      }}
    >
      <Card
        style={{
          fontFamily: 'Roboto,sans-serif',
          boxSizing: 'border-box',
          borderRadius: '5px',
          backgroundColor: '#fafafa',
          borderStyle: 'solid',
          borderColor: 'rgba(128,128,128,0.73)',
          margin: '1% 1%',
          overflow: 'auto'
        }}
      >
        <Typography style={{ margin: '2%' }} variant="h5" component="div">
          {storageType}
        </Typography>
        <div
          style={{
            backgroundColor: '#448ef7',
            width: '80%',
            height: '5px',
            marginLeft: '10%'
          }}
        />
        <Typography
          style={{
            margin: '2%',
            overflow: 'auto',
            wordWrap: 'break-word',
            whiteSpace: 'pre-wrap',
            textOverflow: 'ellipsis',
            display: '-webkit-box',
            lineClamp: 3
          }}
          variant="body2"
        >
          path:{storagePath}
        </Typography>

        <Button
          variant="contained"
          style={{ color: 'white', backgroundColor: '#448ef7', margin: '4%' }}
          size="small"
          onClick={handleSyncStorage}
        >
          Sync Storage
        </Button>
      </Card>
    </Container>
  );
};

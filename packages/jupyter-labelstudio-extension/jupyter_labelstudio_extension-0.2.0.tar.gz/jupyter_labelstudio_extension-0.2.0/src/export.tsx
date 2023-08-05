import React, { useState } from 'react';
import { requestAPI } from './handler';

// eslint-disable-next-line @typescript-eslint/naming-convention
// export interface UserInformation {
//   user: string;
//   apiKey: string;
// }

enum ExportFormat {
  JSON,
  CSV
}

// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
const ExportPanel = (props: any) => {
  // const [userInfo, setUserInfo] = useState(props);

  const { projectID } = props;
  const [currentFormat, setFormat] = useState(ExportFormat[0]);

  async function exportAPI() {
    //TODO: add more export format

    try {
      const reply = await requestAPI<any>('export', {
        body: JSON.stringify({
          project_id: projectID,
          format: currentFormat
        }),
        method: 'POST'
      });
      console.log(reply);
      alert('Successfully export annotation file');
    } catch (reason) {
      console.error(
        `Error on POST /jupyterlab_labelstudio_extension/export.\n${reason}`
      );
      alert('Failed to export.You could try another export format.');
    }
  }

  return (
    <div style={{ marginLeft: '2%' }}>
      <input
        type="radio"
        name="type"
        value="JSON"
        id="exportJSON"
        onChange={() => {
          setFormat(ExportFormat[0]);
        }}
        defaultChecked
      />
      <label htmlFor="exportJSON">JSON</label>
      <input
        type="radio"
        name="type"
        value="CSV"
        id="exportCSV"
        onChange={() => {
          setFormat(ExportFormat[1]);
        }}
      />
      <label htmlFor="exportCSV">CSV</label>
      <br />
      {/*TODO: support CSV(seems to be buggy)*/}
      <button onClick={exportAPI}>Export</button>
    </div>
  );
};

export default ExportPanel;

import React from 'react';

export default function InstructionPage() {
  return (
    <div style={{ marginLeft: '2%' }}>
      <h1>Label Studio Setup Instruction</h1>
      <p>
        {' '}
        It seems you haven't setup a label-studio server on localhost, please
        follow the instruction here to launch the label-studio server on
        http://localhost:8080 with one .ipynb notebook: <link></link>
      </p>
      <br />
    </div>
  );
}

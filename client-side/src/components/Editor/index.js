import React from "react";

import MonacoEditor from 'react-monaco-editor';

const CodeEditorWindow = ({ language, code,handleChangeEditor }) => {
  return (
    <div>
      <MonacoEditor
        width={`100%`}
        height="600"
        language={language || "python"}
        value={code}
        theme= "vs-dark"
        onChange={handleChangeEditor}
      />
    </div>
  );
};
export default CodeEditorWindow;
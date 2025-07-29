
import React, { useState, useEffect } from 'react';

const MarkdownEditor = ({ onContentChange }) => {
  const [content, setContent] = useState('');

  useEffect(() => {
    onContentChange(content);
  }, [content]);

  return (
    <div>
      <h3>Markdown Content</h3>
      <textarea
        placeholder="Write markdown content here..."
        rows={10}
        cols={50}
        value={content}
        onChange={e => setContent(e.target.value)}
      />
    </div>
  );
};

export default MarkdownEditor;

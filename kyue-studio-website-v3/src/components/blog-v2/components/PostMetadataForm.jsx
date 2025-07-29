
import React, { useState, useEffect } from 'react';

const PostMetadataForm = ({ onMetadataChange }) => {
  const [title, setTitle] = useState('');
  const [tags, setTags] = useState('');
  const [summary, setSummary] = useState('');

  useEffect(() => {
    onMetadataChange({
      title,
      tags: tags.split(',').map(tag => tag.trim()),
      summary,
    });
  }, [title, tags, summary]);

  return (
    <div>
      <h3>Post Metadata</h3>
      <input placeholder="Title" value={title} onChange={e => setTitle(e.target.value)} /><br />
      <input placeholder="Tags (comma separated)" value={tags} onChange={e => setTags(e.target.value)} /><br />
      <textarea placeholder="Summary" value={summary} onChange={e => setSummary(e.target.value)} /><br />
    </div>
  );
};

export default PostMetadataForm;

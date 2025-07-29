
import React, { useState, useRef } from 'react';
import PostMetadataForm from './components/PostMetadataForm';
import MarkdownEditor from './components/MarkdownEditor';
import UploadThumbnail from './components/UploadThumbnail';
import api from '../../api/fastapi';

const CreateBlogPostForm = () => {
  const [metadata, setMetadata] = useState({ title: '', tags: [], summary: '' });
  const [markdown, setMarkdown] = useState('');
  const [thumbnailFile, setThumbnailFile] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();

    if (thumbnailFile) {
      formData.append('thumbnail', thumbnailFile);
    }

    const blob = new Blob([markdown], { type: 'text/markdown' });
    const filename = 'post-content.md';
    formData.append('content', blob, filename);

    const metadataObj = {
      ...metadata,
      thumbnail_url: thumbnailFile ? `/uploads/${thumbnailFile.name}` : null,
      content_filename: filename,
    };

    formData.append('metadata', JSON.stringify(metadataObj));

    await api.post('/blog/create-post', formData);
    // await api.post('/blog/create-post', {
    //   method: 'POST',
    //   body: formData,
    // });

    alert('Post submitted!');
    console.log("🟡 Metadata JSON Preview:", metadataObj);
  };

  return (
    <form onSubmit={handleSubmit}>
      <PostMetadataForm onMetadataChange={setMetadata} />
      <UploadThumbnail onFileSelect={setThumbnailFile} />
      <MarkdownEditor onContentChange={setMarkdown} />
      <button type="submit">Submit</button>
    </form>
  );
};

export default CreateBlogPostForm;

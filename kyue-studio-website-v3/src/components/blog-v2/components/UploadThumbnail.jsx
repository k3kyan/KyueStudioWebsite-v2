
import React from 'react';

const UploadThumbnail = ({ onFileSelect }) => {
  const handleChange = (e) => {
    const file = e.target.files[0];
    if (file) onFileSelect(file);
  };

  return (
    <div>
      <h3>Thumbnail Upload</h3>
      <input type="file" accept="image/*" onChange={handleChange} />
    </div>
  );
};

export default UploadThumbnail;

import React, { useState } from "react";

// https://stackoverflow.com/questions/43692479/how-to-upload-an-image-in-react-js

const UploadThumbnail = ({onThumbnailSelect }) => {
  const [selectedImage, setSelectedImage] = useState(null);

  const handleChange = (event) => {
    const file = event.target.files[0];
    setSelectedImage(file);
    onThumbnailSelect(file); // pass file to parent
    console.log(event.target.files[0]); // Log the selected file
  };
  
  return (
    <div>
      {/* Header */}
      <h1>Upload and Display Image</h1>

      {/* Conditionally render the selected image if it exists */}
      {selectedImage && (
        <div>
          {/* Display the selected image */}
          <img
            alt="not found"
            width={"250px"}
            src={URL.createObjectURL(selectedImage)}
          />
          <br /> <br />
          {/* Button to remove the selected image */}
          <button onClick={() => setSelectedImage(null)}>Remove</button>
        </div>
      )}

      <br />

      {/* Input element to select an image file */}
      <input
        type="file"
        name="myImage"
        // Event handler to capture file selection and update the state
        onChange={handleChange}
        // onChange={(event) => {
        //   console.log(event.target.files[0]); // Log the selected file
        //   setSelectedImage(event.target.files[0]); // Update the state with the selected file
        // }}
      />
    </div>
  )
}

export default UploadThumbnail

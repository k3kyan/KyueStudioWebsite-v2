import React from 'react'
// import library for rich text editor that exports as md
import LexicalRichTextEditor from '../lexical-text-editor/LexicalRichTextEditor'
import UploadThumbnail from '../upload-thumbnail/UploadThumbnail'
import PostMetadataForm from '../post-metadata-form/PostMetadataForm'

const CreateBlogPostForm = () => {
  return (
    <div>
        <h3>blog post creation form </h3> 
        <LexicalRichTextEditor />   
        <UploadThumbnail /> {/* TODO: Component: Upload photo for thumbnail (backend prob resizes it...?) */}
        <PostMetadataForm />
    </div>
  )
}

export default CreateBlogPostForm

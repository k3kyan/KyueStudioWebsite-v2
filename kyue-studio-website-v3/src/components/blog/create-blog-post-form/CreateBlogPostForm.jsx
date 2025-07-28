import React from 'react'
// import library for rich text editor that exports as md
// import { RichTextEditor } from '@lexical/react/LexicalRichTextEditor'
import RichTextEditor from './RichTextEditor'

// TODO: ToolbarPlugin - renders UI to control text formatting
// TODO: TreeViewPlugin - renders debug view below the editor so we can see its state in real time

const CreateBlogPostForm = () => {
  return (
    <div>
      blog post creation form 
      {/* react form that exports as md? maybe included in whatever library i find ????  */}
      <RichTextEditor />
    </div>
  )
}

export default CreateBlogPostForm

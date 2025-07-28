import React from 'react'
// import library for rich text editor that exports as md
import RichTextEditor from './RichTextEditor'
import LexicalRichTextEditor from '../lexical-text-editor/LexicalRichTextEditor'
import { ThemeProvider } from '@aws-amplify/ui-react'
// import themeED from './themeED'

const CreateBlogPostForm = () => {
  return (
    <div>
        blog post creation form 
        {/* react form that exports as md? maybe included in whatever library i find ????  */}
        {/* <ThemeProvider theme={themeED}> */}
            {/* <RichTextEditor /> */}
        {/* </ThemeProvider> */}
        <LexicalRichTextEditor />   
    </div>
  )
}

export default CreateBlogPostForm

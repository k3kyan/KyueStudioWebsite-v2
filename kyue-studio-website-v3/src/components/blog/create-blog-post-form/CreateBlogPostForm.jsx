import React from 'react'
// import library for rich text editor that exports as md
import LexicalRichTextEditor from '../lexical-text-editor/LexicalRichTextEditor'
import UploadThumbnail from '../upload-thumbnail/UploadThumbnail'
import PostMetadataForm from '../post-metadata-form/PostMetadataForm'
// import {$generateMarkdownFromNodes} from '@lexical/markdown'
import { useState, useRef} from 'react'

const CreateBlogPostForm = () => {
    // all fields
    const [title, setTitle] = useState('');
    const [tags, setTags] = useState([]);
    const [summary, setSummary] = useState('');
    const [thumbnailFile, setThumbnailFile] = useState(null);
    const [editorState, setEditorState] = useState(null); // This comes from Lexical
    const editorRef = useRef(null);
    // const editorRef = useRef<LexicalEditorHandle>(null);

    console.log({ title, tags, summary, thumbnailFile, editorRef });

    // Lexical: Convert editor content to Markdown
    const handleEditorChange = (editor) => {
    const markdown = editor.getEditorState().read(() =>
        $generateMarkdownFromNodes(editor, transformers)
    );
    setEditorState(markdown);
    };


    // Form Submission
    const handleSubmit = async (e) => {
        e.preventDefault();

        // 1. Upload thumbnail
        const thumbnailFormData = new FormData();
        thumbnailFormData.append('file', thumbnailFile);
        const thumbnailRes = await fetch('/api/upload-thumbnail', {
            method: 'POST',
            body: thumbnailFormData
        });
        const { filePath: thumbnailPath } = await thumbnailRes.json();

        // 2. Upload content as .md
        // // const markdownContent = await editorRef.current.getMarkdown(); // TODO ????????????
        const markdown = editorRef.current?.getMarkdown() ?? ''; // TODO ????????????
        // console.log('Editor Markdown:', markdown); // TODO ????????????
        // const contentBlob = new Blob([editorState], { type: 'text/markdown' });
        // const contentFormData = new FormData();
        // // contentFormData.append('file', markdownContent, 'content.md'); //TODO: ???? maybe replace contentBlog with markdownContent 
        // contentFormData.append('file', contentBlob, 'content.md'); //TODO: ???? maybe replace contentBlog with markdownContent 
        const markdownContent = editorRef.current?.getMarkdown() ?? '';
        const contentBlob = new Blob([markdownContent], { type: 'text/markdown' });
        const contentFormData = new FormData();
        contentFormData.append('file', contentBlob, 'content.md');
        const contentRes = await fetch('/api/upload-content', {
            method: 'POST',
            body: contentFormData
        });
        const { filePath: contentPath } = await contentRes.json();

        // 3. Send metadata
        const metadata = {
            title,
            tags,
            summary,
            thumbnailPath,
            contentPath,
        };
        await fetch('/api/create-post', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify(metadata)
        });
    };



  return (
    <form onSubmit={handleSubmit}>
        <h3>blog post creation form </h3> 
        <LexicalRichTextEditor ref = {editorRef} />   {/* Should I be passing in children or plugins ?? */}
        <UploadThumbnail onThumbnailSelect={setThumbnailFile} /> {/* TODO: Component: Upload photo for thumbnail (backend prob resizes it...?) */}
        <PostMetadataForm
            onMetadataChange={({ title, tags, summary }) => {
                setTitle(title);
                setTags(tags);
                setSummary(summary);
            }}
        />
      <button type="submit">Submit</button>
    </form>
  )
}

export default CreateBlogPostForm

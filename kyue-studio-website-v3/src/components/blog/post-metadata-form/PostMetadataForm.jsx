// import React, { useState } from 'react';
import React, { useState, useEffect } from 'react';

// NOTE: does not submit anything itself, needs that function passed in from the parent
// so does not use import api here, its JUST a form component.



// {/* TODO: react form that exports as md? maybe included in whatever library i find ????  */}
//     {/* TODO: Component: Form for blog post metadata */}  

// NEEDS A SPECIAL FORM FOR THIS KIND OF SUBMISSION ...?? IDK

// REFERENCE FRUIT API FORM FILE 

const PostMetadataForm = ({onMetadataChange}) => {
    // Metadata Fields
    const [title, setTitle] = useState('');
    // const [description, setDescription] = useState('');
    const [tags, setTags] = useState(''); // TODO: useState([]);
    const [summary, setSummary] = useState('');

    useEffect(() => {
      onMetadataChange({ title, tags: tags.split(','), summary });
    }, [title, tags, summary]);

    // const handleSubmit = (event) => {
    //     event.preventDefault();
    //     if (fruitName) {
    //         onSubmit(fruitName);
    //         setTitle('');
    //         setDescription('');
    //         setTags([]);
    //         setSummary('');
    //     }
    // };

  return (
    <div>
      <input value={title} onChange={(e) => setTitle(e.target.value)} />
      <input value={tags} onChange={(e) => setTags(e.target.value)} />
      <input value={summary} onChange={(e) => setSummary(e.target.value)} />
    </div>

    // <form onSubmit={handleSubmit}>
    //   <h2>Post Metadata Form</h2>
    //   <input
    //     type="text"
    //     value={title}
    //     onChange={(e) => setTitle(e.target.value)}
    //     placeholder="Title /////// TODO: Post Information/Meta Form // Reference TempFruitsAPIForm.jsx"
    //   />
    //   <input
    //     type="text"
    //     value={description}
    //     onChange={(e) => setDescription(e.target.value)}
    //     placeholder="description"
    //   />
    //   <input
    //     type="text"
    //     value={tags}
    //     onChange={(e) => setTags(e.target.value)}
    //     placeholder="tags"
    //   />
    //   <input
    //     type="text"
    //     value={summary}
    //     onChange={(e) => setSummary(e.target.value)}
    //     placeholder="summary"
    //   />

    //   <button type="submit">Submit Blog Post Info</button>
    // </form>
  )
}

export default PostMetadataForm

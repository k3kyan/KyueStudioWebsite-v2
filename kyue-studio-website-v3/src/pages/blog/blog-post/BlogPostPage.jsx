import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import api from '../../../api/fastapi';
import ReactMarkdown from 'react-markdown';
import { Link } from 'react-router-dom';
import { useAuth } from '../../../../GlobalContext';
import { Navigate, useNavigate } from 'react-router-dom';
// USE DELETE ENDPOINT HERE!!! also validate that only author can delete it in frontend

const BlogPostPage = () => {
    const { post_id } = useParams(); // fetched parameters must match varname in the route <Route path="/blog/post/:post_id
    const [post, setPost] = useState(null);
    const [content, setContent] = useState("");
    const [error, setError] = useState(null);
    const { isLoggedIn } = useAuth();  
    const navigate = useNavigate();

  useEffect(() => {
    const fetchPost = async () => {
      try {
        // const res = await fetch(`http://localhost:8000/blog/post/${post_id}`);
        const res = await api.get(`/blog/post/${post_id}`); //#FIX!!!! NEED THIS FOR DYNAMICS
        // const res = await api.get(`/blog/post/48f4d4fd-7aef-4801-87ab-b811837582ed`); // hardcoded, works
        // const data = await res.json();
        const data = res.data;
        setPost(data);

        const contentRes = await fetch(`http://localhost:8000/content/${data.content_filename}`); // TODO: replace with a better localhost idk why this doesnt work
        // const contentRes = await fetch(`http://localhost:8000/content/0380b2d8-187c-4403-a0fa-7a0141d5d0eb_content.md`); // HARDCODED, WORKS // idk how to make it dynamic, might be an issue for aws 
        // const text = await contentRes.text();
        // const text = contentRes.text();
        // setContent(text);
        const text = await contentRes.text();
        setContent(text);
      } catch (err) {
        setError("Failed to load blog post.");
        console.error(err);
      }
    };

    fetchPost();
  }, [post_id]);

  if (error) return <div>{error}</div>;
  if (!post) return <div>Loading...</div>;

    //   Delete Post endpoint
  const handleDeletePost = async (event) => {
    event.preventDefault();
    try {
        // await api.delete('/blog/post/${post_id}')
        await api.delete(`/blog/post/${post_id}`);

        // redirect to blog page after post is deleted
        // Navigate('/blog');
        // return <Navigate to="/" />
        alert('Post deleted!');
        navigate("/blog");
    } catch (err) {
        console.error("Failed to delete:", err);
        setError("Failed to delete blog post.");
    }
  };


  return (
    <div className="post-container">
      <Link to="/blog">Back to Blog</Link>
        {/* Admin Update Delete crud operations */}
        {/* Conditional Rendering for Protected Routes (Admin stuff) */}
        {isLoggedIn && ( // REPLACE WITH VARIABLE BOOL ON WHETHER UR LOGGED IN OR NOT
            <button onClick = {handleDeletePost}>Delete Post</button>
        )}


      <h1>{post.title}</h1>
      <img src={'http://localhost:8000/thumbnails/' + post.thumbnail_url} alt={post.title} /> {/* TODO: IMPORTANT: NEED TO CHANGE THIS LOCALHOST !!!! */}
      <p>{post.summary}</p>
      <div>
        <strong>Tags:</strong> {post.tags.join(", ")}
      </div>
      <div>
        <strong>Date:</strong> {new Date(post.date_created).toLocaleDateString()}
      </div>
      <hr />
      <div>
        {/* <pre style={{ whiteSpace: 'pre-wrap' }}>{content}</pre> */}
        <ReactMarkdown>{content}</ReactMarkdown>
      </div>
    </div>
  );
//   const { postId } = useParams();
//   const [metadata, setMetadata] = useState(null);

//   useEffect(() => {
//     const fetchPost = async () => {
//       const res = await fetch(`http://localhost:8000/blog/post/${postId}`);
//       const data = await res.json();
//       setMetadata(data);
//     };
//     fetchPost();
//   }, [postId]);

//   if (!metadata) return <div>Loading...</div>;

//   return (
//     <div>
//       <h1>{metadata.title}</h1>
//       <img src={metadata.thumbnail_url} alt={metadata.title} />
//       <p>{metadata.summary}</p>
//       {/* load and display markdown content too if needed */}
//     </div>
//   );
};

export default BlogPostPage;

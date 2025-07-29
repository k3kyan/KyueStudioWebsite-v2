import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import api from '../../../api/fastapi';
// USE DELETE ENDPOINT HERE!!! also validate that only author can delete it in frontend

const BlogPostPage = ({post_id}) => {
    
  const { post_id } = useParams();
  const [post, setPost] = useState(null);
  const [content, setContent] = useState("");
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPost = async () => {
      try {
        const res = await fetch(`http://localhost:8000/blog/post/${post_id}`);
        const data = await res.json();
        setPost(data);

        const contentRes = await fetch(`http://localhost:8000/uploads/blog_content/${data.content_filename}`);
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

  return (
    <div className="post-container">
      <h1>{post.title}</h1>
      <img src={post.thumbnail_url} alt={post.title} />
      <p>{post.summary}</p>
      <div>
        <strong>Tags:</strong> {post.tags.join(", ")}
      </div>
      <div>
        <strong>Date:</strong> {new Date(post.date_created).toLocaleDateString()}
      </div>
      <hr />
      <div>
        <pre style={{ whiteSpace: 'pre-wrap' }}>{content}</pre>
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

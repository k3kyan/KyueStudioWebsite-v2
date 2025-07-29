import { useState } from 'react'
import './App.css'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Header from './components/header/Header';
import Footer from './components/footer/Footer';
import Home  from './pages/home/Home'
import About from './pages/about/About'
import Shop from './pages/shop/Shop';
import Blog from './pages/blog/Blog';
import Art from './pages/art/Art';
import Login from './pages/login/Login';
import AdminDashboard from './pages/admin/dashboard/AdminDashboard';
import AdminCreateBlogPost from './pages/admin/create-blog-post/AdminCreateBlogPost';
import AdminCreateArtPost from './pages/admin/create-art-post/AdminCreateArtPost';
import AdminOrders from './pages/admin/orders/AdminOrders';
import AdminMessageBoard from './pages/admin/messages/AdminMessageBoard';



import { AuthorizationProvider } from '../GlobalContext'; // CAUTION: correct path...?
import { useAuth } from '../GlobalContext';

function App() {
  return (
    <BrowserRouter>
      <AuthorizationProvider>
        <Header />

        <main style={{ padding: '0 4rem 4rem' }}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/index.html" element={<Home />} />

            <Route path="/blog" element={<Blog />} />
            {/* <Route path="/blog/post/:postId" element={<BlogPostPage />} />  */}
            {/* MAY HAVE SOME MISMATCHED ROUTING */}

            <Route path="/art" element={<Art />} />
            <Route path="/shop" element={<Shop />} />
            <Route path="/about" element={<About />} />
            <Route path="*" element={<h1>404 - Not Found</h1>} />

            
            <Route path="/login" element={<Login />} />
            {/* Protected Routes/Pages */}
            {/* I think to make these protected routes, you have to redirect to homepage if ur not logged in, right from the page itself ...? so not here ...? */}
            {/* TODO: make a sidebar that appears when logged in for admin pages..?*/}
            <Route path="/admin/dashboard" element={<AdminDashboard />} />
            <Route path="/admin/messages" element={<AdminMessageBoard />} />
            <Route path="/admin/orders" element={<AdminOrders />} />
            <Route path="/admin/create-blog-post" element={<AdminCreateBlogPost />} />
            <Route path="/admin/create-art-post" element={<AdminCreateArtPost />} />
          </Routes>
        </main>

        <Footer />
      </AuthorizationProvider>
    </BrowserRouter>
  );
}

export default App;

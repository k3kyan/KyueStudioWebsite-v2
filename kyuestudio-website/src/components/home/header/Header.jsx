import React from 'react'
// import '../../../App.css';
// import '../../../index.css';
import Logo from '../../../assets/images/KyueStudioLogo.jpg';

const Header = () => {
  return (
    <>
      <header className="header">
        <div className="">

            <div className="flex justify-between font-bold">
                <img src={Logo} className="logo" alt="Kyue Studio Logo" />
                Kyue Studio
            </div>

            <div className="flex gap-[15px]">
                <nav>
                    <a href="">Home</a>
                    <a href="">Blog</a>
                    <a href="">Projects</a>
                    <a href="">Shop</a>
                    <a href="">About</a>
                </nav>
            </div>

        </div>

      </header>
      {/* <h1 className="text-7xl text-center text-blue-500">Header Nav Bar</h1> */}
    </>
  )
}

export default Header

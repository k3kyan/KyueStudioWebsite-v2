import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],

  // routing, necessary for using ReactRouter with Vite and S3 and CloudFront
  build: {
    outDir: 'dist',
  },
  base: '/',
})

# SmartHome Landing Page

Modern React landing page for a smart home company with temperature monitoring integration.

## Features

- **Responsive Design** - Works on desktop and mobile
- **Modern UI** - Beautiful gradient design with animations
- **Temperature Monitoring** - Real-time temperature data from PythonAnywhere API
- **Contact Form** - Interactive contact form with validation
- **Company Information** - About page with team and company details

## Pages

- **Home** - Hero section with features and call-to-action
- **About** - Company story, mission, vision, team, and statistics
- **Temperature** - Real-time temperature monitoring and history
- **Contact** - Contact form and company information

## Setup

### Prerequisites
- Node.js (v14 or higher)
- npm or yarn

### Installation

1. **Clone or download the project**
2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Configure API URL:**
   Edit `src/components/Temperature.js` and replace:
   ```javascript
   const API_BASE_URL = 'https://YOUR_USERNAME.pythonanywhere.com';
   ```
   With your actual PythonAnywhere API URL.

4. **Start development server:**
   ```bash
   npm start
   ```

5. **Open browser:**
   Navigate to `http://localhost:3000`

## Build for Production

```bash
npm run build
```

This creates a `build` folder with optimized production files.

## Deployment

### Netlify (Recommended)
1. Push code to GitHub
2. Connect repository to Netlify
3. Set build command: `npm run build`
4. Set publish directory: `build`
5. Deploy

### Vercel
1. Install Vercel CLI: `npm i -g vercel`
2. Run: `vercel`
3. Follow prompts

### GitHub Pages
1. Add to package.json:
   ```json
   "homepage": "https://YOUR_USERNAME.github.io/REPO_NAME",
   "scripts": {
     "predeploy": "npm run build",
     "deploy": "gh-pages -d build"
   }
   ```
2. Install gh-pages: `npm install --save-dev gh-pages`
3. Deploy: `npm run deploy`

## API Integration

The Temperature page fetches data from the PythonAnywhere API:

- **Current Temperature**: `GET /temperature`
- **Temperature History**: `GET /temperatures`
- **Add Temperature**: `POST /temperature`
- **Delete Temperature**: `DELETE /temperature/{id}`

## Project Structure

```
src/
├── components/
│   ├── Navbar.js          # Navigation component
│   ├── Home.js            # Home page
│   ├── About.js           # About page
│   ├── Contact.js         # Contact page
│   ├── Temperature.js     # Temperature monitoring
│   ├── Footer.js          # Footer component
│   └── *.css              # Component styles
├── App.js                 # Main app with routing
├── index.js              # App entry point
└── index.css             # Global styles
```

## Technologies Used

- **React** - Frontend framework
- **React Router** - Client-side routing
- **Axios** - HTTP client for API calls
- **CSS3** - Styling with modern features
- **Responsive Design** - Mobile-first approach

## Customization

### Colors
Main colors are defined in CSS variables in `src/index.css`:
- Primary: `#667eea` to `#764ba2` (gradient)
- Secondary: `#2ed573` to `#1e90ff` (gradient)

### Content
Edit component files to customize:
- Company information in `About.js`
- Contact details in `Contact.js`
- Features in `Home.js`

### API Configuration
Update the API URL in `Temperature.js` to point to your deployed PythonAnywhere API.

## Troubleshooting

### API Connection Issues
1. Check if PythonAnywhere API is running
2. Verify API URL in `Temperature.js`
3. Check browser console for CORS errors
4. Ensure API endpoints are working

### Build Issues
1. Clear node_modules: `rm -rf node_modules`
2. Reinstall: `npm install`
3. Clear cache: `npm start -- --reset-cache`

## Support

For issues or questions:
1. Check browser console for errors
2. Verify API connectivity
3. Ensure all dependencies are installed
4. Check React Router configuration

## License

MIT License - feel free to use and modify for your projects. 
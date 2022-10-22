import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, } from 'react-router-dom';
import { ColorModeScript, ChakraProvider } from '@chakra-ui/react';
import { SWRConfig } from 'swr';
import type { Fetcher, SWRConfiguration } from 'swr';

import { Auth0Provider } from '@auth0/auth0-react';
// import { render } from 'react-dom';

import theme from './theme';
import App from './App';



const domain = import.meta.env.VITE_AUTH0_DOMAIN;
const clientId = import.meta.env.VITE_AUTH0_CLIENT_ID;

// const domain = process.env.REACT_APP_AUTH0_DOMAIN;
// const clientId = process.env.REACT_APP_AUTH0_CLIENT_ID;
 if (!domain || !clientId) {
    throw new Error("Missing Environment Variable!")
}; 

class ApiError extends Error {
  info?: any;

  status?: number;

  constructor(message?: string) {
    super(message);
    this.name = 'ApiError';
    Object.setPrototypeOf(this, new.target.prototype);
  }
}

const fetcher: Fetcher = async (url: string) => {
  const res = await fetch(url);

  if (!res.ok) {
    const error = new ApiError('An error occurred while fetching the data.');
    error.info = await res.json();
    error.status = res.status;
    throw error;
  }

  return res.json();
};

const swrConfig: SWRConfiguration = { fetcher };

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(

    <React.StrictMode>
      <ColorModeScript initialColorMode={theme.config.initialColorMode} />
      <BrowserRouter>
        <ChakraProvider theme={theme}>
          <SWRConfig value={swrConfig}>
            <Auth0Provider
              domain={domain}
              clientId={clientId}
              redirectUri={window.location.origin}
            >
              <App />
            </Auth0Provider>
          </SWRConfig>
        </ChakraProvider>
      </BrowserRouter>
    </React.StrictMode>,
  
); 

/* 
ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(

    <React.StrictMode>
      <ColorModeScript initialColorMode={theme.config.initialColorMode} />
      <BrowserRouter>
        <ChakraProvider theme={theme}>
          <SWRConfig value={swrConfig}>
            <App />
          </SWRConfig>
        </ChakraProvider>
      </BrowserRouter>
    </React.StrictMode>
); 
*/
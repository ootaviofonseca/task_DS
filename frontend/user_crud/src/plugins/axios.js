import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://localhost:5000/api',  // URL of the backend server
  timeout: 1000,
});


export default axiosInstance;

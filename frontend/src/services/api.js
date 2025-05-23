import axios from 'axios';

const API_URL = 'http://localhost:8000/api/agents/dispatch/'; // Cambia se usi un dominio/backend diverso

export async function dispatchAgent(agent_type, input_data) {
  const response = await axios.post(API_URL, { agent_type, input_data });
  return response.data;
}

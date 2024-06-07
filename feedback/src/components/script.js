import axios from 'axios'

const API_URL = "http://localhost:8000/api/ratings"

export async function getRating(data){
    try {
        const response = await axios.get(API_URL);
        data.rating = response.data.data.rating;
    } catch (error) {
        data.error = error;
    } finally {
        data.isLoading = false;
    }
    return data
}

export async function submit(payload, data){
    try {
      await axios.post(API_URL, payload)
    } catch (error) {
      data.error = error;
    }
    return data
}

export function handleClicked(data,target){
    for (let i=0;i < data.length;i++){
      if (i <= target){
        data[i].isClicked = true
      }else{
        data[i].isClicked = false
      }
    }
}
import { create } from "zustand";
import axios from "axios";

const { BASE_URL } = import.meta.env.BASE_URL;

const useUserStorage = create((set) => ({
  token: null,
  user: 1,
  getUserToken: (userName, password) => {
    const raw = { userName: userName, password: password };
    const newToken = axios.get(`${BASE_URL}/user/token/`, raw);
    console.log(newToken);
    set({ token: newToken });
  },
  setUser: (newUser) => set({ user: newUser }),
}));

export default useUserStorage;

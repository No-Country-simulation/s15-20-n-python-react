import { create } from "zustand";
import axios from "axios";

const { BASE_URL } = import.meta.env.BASE_URL;

const useUserStorage = create((set) => ({
  token: null,
  user: {
    username: "Admin",
    email: "pachecolobos.felix@gmail.com",
    projects: [
      {
        project_id: 2,
        name: "Mi primer proyecto",
        teams: [],
        collabs: [],
        is_active: true,
      },
      {
        project_id: 1,
        name: "Primer proyecto",
        teams: [],
        collabs: [],
        is_active: true,
      },
    ],
  },
  getUserToken: (userName, password) => {
    const raw = { userName: userName, password: password };
    const newToken = axios.get(`${BASE_URL}/user/token/`, raw);
    console.log(newToken);
    set({ token: newToken });
  },
  setUser: (newUser) => set({ user: newUser }),
}));

export default useUserStorage;

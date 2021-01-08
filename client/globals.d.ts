// 1. Make sure to import 'vue' before declaring augmented types
import Vue from 'vue'

interface AuthUser {
  user_id: string, 
  name: string,
  nickname: string,
  picture: string,
  given_name: string,
  family_name: string
}

interface AuthObject {
  loading: boolean,
  isAuthenticated: boolean,
  user: AuthUser,
  auth0Client: string,
  popupOpen: boolean,
  error: string
}

// 2. Specify a file with the types you want to augment
//    Vue has the constructor type in types/vue.d.ts
declare module 'vue/types/vue' {
  // 3. Declare augmentation for Vue
  interface Vue {
    $auth: AuthObject
  }
}
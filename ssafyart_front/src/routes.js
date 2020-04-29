import Main from '@/components/Main.vue'
import Create from '@/components/Create.vue'
import Result from '@/components/Result.vue'
import Gallery from '@/components/Gallery.vue'
import About from '@/components/About.vue'
import Error404 from '@/components/404.vue'

export default [
  {
    path : '/',
    name : 'Main',
    component : Main,
    meta: {loginRequire: false}
  },
  {
    path : '/create',
    name : 'Create',
    component : Create,
    meta: {loginRequire: true}
  },
  {
    path : '/result',
    name : 'Result',
    component : Result,
    meta: {loginRequire: true}
  },
  {
    path : '/gallery',
    name : 'Gallery',
    component : Gallery,
    meta: {loginRequire: true}
  },
  {
    path : '/about',
    name : 'About',
    component : About,
    meta: {loginRequire: false}
  },
  {
    path : '/*',
    name : Error404,
    component : Error404,
    meta: {loginRequire: false}
  }
]
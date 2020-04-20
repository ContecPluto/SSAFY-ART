import Main from '@/components/Main.vue'
import Create from '@/components/Create.vue'
import Result from '@/components/Result.vue'

export default [
  {
    path : '/',
    name : 'Main',
    component : Main,
  },
  {
    path : '/create/',
    name : 'Create',
    component : Create 
  },
  {
    path : '/result/',
    name : 'Result',
    component : Result
  }
]
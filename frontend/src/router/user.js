export default {
  path: '/user',
  name: 'user',
  component: () => import('@/layouts/UserLayout'),
  redirect: '/user/login',
  children: [
    {
      path: 'login',
      name: 'login',
      meta: { title: '登录' },
      component: () => import('@/views/login/Login'),
    },
    {
      path: 'register',
      name: 'register',
      meta: { title: '注册' },
      component: () => import('@/views/register/Register'),
    },
    // {
    //   path: 'set_password',
    //   name: 'setPassword',
    //   meta: { title: '设置密码' },
    //   component: () => import('@/views/setPassword/SetPassword'),
    // },
  ],
}

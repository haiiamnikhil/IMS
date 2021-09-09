import { FirmSignupComponent } from './auth/firmsignup/firmsignup.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SigninComponent } from './auth/signin/signin.component';
import { UserSignupComponent } from './auth/usersignup/usersignup.component';
import { GetstartedComponent } from './getstarted/getstarted.component';


const routes: Routes = [
  {
    path: 'auth/signin', component: SigninComponent
  },
  {
    path: 'signup/user', component: UserSignupComponent
  },
  {
    path: 'signup/firm', component: FirmSignupComponent
  },
  {
    path: 'getstarted', component: GetstartedComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

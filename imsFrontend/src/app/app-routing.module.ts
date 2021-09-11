import { FirmSignupComponent } from './auth/firmsignup/firmsignup.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SigninComponent } from './auth/signin/signin.component';
import { UserSignupComponent } from './auth/usersignup/usersignup.component';
import { GetstartedComponent } from './getstarted/getstarted.component';
import { DashboardComponent } from './main/dashboard/dashboard.component';
import { ListuserComponent } from './user/listuser/listuser.component';


const routes: Routes = [
  {
    path: 'home', component: DashboardComponent,
  },
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
  },
  {
    path: 'list-user', component: ListuserComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

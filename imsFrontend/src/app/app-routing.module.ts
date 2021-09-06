import { FirmregisterComponent } from './auth/firmregister/firmregister.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SigninComponent } from './auth/signin/signin.component';
import { SignupComponent } from './auth/signup/signup.component';
import { FirmsigninComponent } from './auth/firmsignin/firmsignin.component';


const routes: Routes = [
  {
    path: 'auth/signin/user', component: SigninComponent
  },
  {
    path: 'auth/signup', component: SignupComponent
  },
  {
    path: 'firm/register-firm', component: FirmregisterComponent
  },
  {
    path: 'auth/signin/firm', component: FirmsigninComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';
import { UserSignupComponent } from './auth/usersignup/usersignup.component';
import { SigninComponent } from './auth/signin/signin.component';
import { FirmSignupComponent } from './auth/firmsignup/firmsignup.component';
import { AuthService } from './services/authservice/auth.service';
import { FirmService } from './services/firm/firm.service';
import { ListuserComponent } from './firm_management/listuser/listuser.component';
import { FirmProfileComponent } from './profile/firm-profile/firm-profile.component';
import { UserProfileComponent } from './profile/user-profile/user-profile.component';
import { GetstartedComponent } from './getstarted/getstarted.component';


@NgModule({
  declarations: [
    AppComponent,
    UserSignupComponent,
    SigninComponent,
    FirmSignupComponent,
    ListuserComponent,
    FirmProfileComponent,
    UserProfileComponent,
    GetstartedComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  providers: [AuthService,FirmService],
  bootstrap: [AppComponent]
})
export class AppModule { }

import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';
import { SignupComponent } from './auth/signup/signup.component';
import { SigninComponent } from './auth/signin/signin.component';
import { FirmregisterComponent } from './auth/firmregister/firmregister.component';
import { AuthService } from './services/authservice/auth.service';
import { FirmService } from './services/firm/firm.service';
import { FirmsigninComponent } from './auth/firmsignin/firmsignin.component';
import { ListuserComponent } from './firm_management/listuser/listuser.component';
import { FirmProfileComponent } from './profile/firm-profile/firm-profile.component';
import { UserProfileComponent } from './profile/user-profile/user-profile.component';

@NgModule({
  declarations: [
    AppComponent,
    SignupComponent,
    SigninComponent,
    FirmregisterComponent,
    FirmsigninComponent,
    ListuserComponent,
    FirmProfileComponent,
    UserProfileComponent
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

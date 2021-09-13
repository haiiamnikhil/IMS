import { BrowserModule, Title } from '@angular/platform-browser';
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
import { FirmProfileComponent } from './profile/firm-profile/firm-profile.component';
import { UserProfileComponent } from './profile/user-profile/user-profile.component';
import { GetstartedComponent } from './getstarted/getstarted.component';
import { DashboardComponent } from './main/dashboard/dashboard.component';
import { NavbarComponent } from './common/navbar/navbar.component';
import { SidebarComponent } from './common/sidebar/sidebar.component';
import { UserService } from './services/user/user.service';
import { CommonService } from './services/common/common.service';
import { CommonModule } from '@angular/common';
import { CreateinvoiceComponent } from './invoice/createinvoice/createinvoice.component';
import { ListinvoiceComponent } from './invoice/listinvoice/listinvoice.component';
import { ListuserComponent } from './user/listuser/listuser.component';


@NgModule({
  declarations: [
    AppComponent,
    UserSignupComponent,
    SigninComponent,
    FirmSignupComponent,
    FirmProfileComponent,
    UserProfileComponent,
    GetstartedComponent,
    DashboardComponent,
    NavbarComponent,
    SidebarComponent,
    CreateinvoiceComponent,
    ListinvoiceComponent,
    ListuserComponent,
  ],
  imports: [
    BrowserModule,
    CommonModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  providers: [AuthService,FirmService,UserService,CommonService,Title],
  bootstrap: [AppComponent]
})
export class AppModule { }

import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/authservice/auth.service';


@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css']
})
export class SigninComponent implements OnInit {

  form: FormGroup;
  isBusy:boolean = false;
  message:string

  constructor(private auth: AuthService, private router: Router, private formBuilder: FormBuilder) { }

  ngOnInit(){
    this.form = this.formBuilder.group({
      email : [null,[Validators.required, Validators.email]],
      password : [null,Validators.required]
    })
  }

  userSignIn(){
    this.isBusy = true;
    let credentials = new FormData();
    credentials.append('username', this.form.get('email').value);
    credentials.append('password', this.form.get('password').value);
    this.auth.userSignIn(credentials).subscribe(response => {
      if (response.success){
        console.log('Logged In')
      } else {
        console.log('Credentials Missmatch')
      }
    }, err => console.log(err))
  }

}

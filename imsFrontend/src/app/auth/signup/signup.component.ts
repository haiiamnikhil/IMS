import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/authservice/auth.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {

  form:FormGroup;
  isBusy:boolean = false;
  message:string;
  messageSuccess:boolean = true;

  constructor(private auth: AuthService, private router: Router, private formBuilder: FormBuilder) { }

  ngOnInit(){
    this.form = this.formBuilder.group({
      email: [null, [Validators.required, Validators.email]],
      first_name: [null, Validators.required], last_name: [null, Validators.required],
      password: [null, Validators.required],
      confirmPassword:[null, Validators.required]
    })
    setTimeout(()=>{
      this.messageSuccess = false
    },3000)
  }

  userSignUp(){
    this.isBusy = true;
    let credentials = {
      username:this.form.get('email').value,
      password:this.form.get('password').value,
      first_name: this.form.get('first_name').value,
      last_name: this.form.get('last_name').value
    }
    this.auth.userSignUp(credentials).subscribe(response => {
      if (response.success){
        console.log(true)
      } else {
        console.log(false)
      }
    }, err => console.log(err))
  }
}

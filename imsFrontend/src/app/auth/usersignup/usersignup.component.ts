import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { FirmService } from 'src/app/services/firm/firm.service';
import { UserService } from 'src/app/services/user/user.service';

@Component({
  selector: 'app-signup',
  templateUrl: './usersignup.component.html',
  styleUrls: ['./usersignup.component.css']
})
export class UserSignupComponent implements OnInit {

  form:FormGroup;
  isBusy:boolean = false;
  message:string;
  messageSuccess:boolean = true;
  firmnames = []
  default = "Select"

  constructor(private auth: UserService, private firm: FirmService, private router: Router, private formBuilder: FormBuilder) { }

  ngOnInit(){
    this.firm.getFirms().subscribe(response => {
      if (response.success){
        for (let i = 0; i < response.data.length; i++){
          this.firmnames.push(response.data[i].firmname);
        }
      } else{
        console.log("Some Error Occured")
      }
    }, err => console.log(err))
    
    this.form = this.formBuilder.group({firmname:[this.default,Validators.required],
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
      user_type : 'firm_user',
      user_firmname: this.form.get('firmname').value,
      email:this.form.get('email').value,
      password:this.form.get('password').value,
      first_name: this.form.get('first_name').value,
      last_name: this.form.get('last_name').value
    }
    this.auth.userSignUp(credentials).subscribe(response => {
      if (response.success){
        this.router.navigate(['/auth/signin'])
      } else {
        this.message = response.message
      }
    }, err => console.log(err))
  }
}

import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { FirmService } from 'src/app/services/firm/firm.service';

@Component({
  selector: 'app-firmsignin',
  templateUrl: './firmsignin.component.html',
  styleUrls: ['./firmsignin.component.css']
})
export class FirmsigninComponent implements OnInit {

  form:FormGroup;
  message:string;
  isBusy:boolean = false;

  constructor(private router: Router, private formBuilder: FormBuilder, private auth: FirmService) { }

  ngOnInit(){
    this.form = this.formBuilder.group({
      email:[null,[Validators.required,Validators.email]],password:[null,Validators.required]
    })
  }

  firmSignIn(){
    this.isBusy = true;
    let credentials = {
      username: this.form.get('email').value, password: this.form.get('password').value
    }
    this.auth.signInFirm(credentials).subscribe(response => {
      if (response.success){
        console.log("Firm Logged in")
      } else{
        this.message = response.message;
        console.log(this.message)
      }
    }, err => console.log(err))
  }

}

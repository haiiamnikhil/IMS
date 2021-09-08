import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { FirmService } from 'src/app/services/firm/firm.service';

@Component({
  selector: 'app-firmsignup',
  templateUrl: './firmsignup.component.html',
  styleUrls: ['./firmsignup.component.css']
})
export class FirmSignupComponent implements OnInit {

  form:FormGroup;
  isBusy:boolean = false;
  message:string;
  changeId:boolean = false;
  firmId:string

  constructor(private firm:FirmService, private router:Router, private formBuilder:FormBuilder) { }

  ngOnInit(){
    this.form = this.formBuilder.group({
      firmname: [null,Validators.required],nnid:[{value:this.firmId,disabled:true},Validators.required],
      password: [null,Validators.required], confirm_pass: [null,Validators.required], email:[null,[Validators.required,Validators.email]]
    })
  }

 makeid() {
    var text = "";
    var possible = "0123456789";
    for (var i = 0; i <= 9; i++)
      text += possible.charAt(Math.floor(Math.random() * possible.length));
    return text;
  }
  
  changeFirmId(event:any){
    console.log(event)
    this.changeId = true
  }

  generateID(event:any){
    this.form.get('nnid').setValue(this.makeid())
  }

  registerFirm(){
    this.isBusy = true
    let firmDetails = {
      user_type:'firm',
      firmname: this.form.get('firmname').value,
      password: this.form.get('password').value,
      email: this.form.get('email').value,
      nnid : this.form.get('nnid').value,
    }

    this.firm.registerFirm(firmDetails).subscribe(response => {
      if (response.success){
        this.router.navigate(['/auth/signin/'])
      } else {
        console.log(false)
      }
    }, err => console.log(err))
  }

}

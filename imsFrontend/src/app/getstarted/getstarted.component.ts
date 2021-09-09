import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { CommonService } from '../services/common/common.service';

@Component({
  selector: 'app-getstarted',
  templateUrl: './getstarted.component.html',
  styleUrls: ['./getstarted.component.css']
})
export class GetstartedComponent implements OnInit {
  
  userDetails:any
  form:FormGroup;

  constructor(private profile:CommonService,private formBuilder:FormBuilder) { }

  ngOnInit(){
    this.profile.onBoardDetails().subscribe(response => {
      if(response.success){
        this.userDetails = response.data
        this.populateData()
        console.log(this.userDetails)
      } else {
        console.log('error')
      }
    }, err => console.log(err))

    this.form = this.formBuilder.group({
      firmname:[{value:null,disabled:true},Validators.required],nnid:[{value:null,disabled:true},Validators.required],
      email:[{value:null,disabled:true},Validators.required]
    })
  }
  populateData(){
    this.form.get('firmname').setValue(this.userDetails.firmname)
    this.form.get('email').setValue(this.userDetails.email)
    this.form.get('nnid').setValue(this.userDetails.nnid)
  }
}

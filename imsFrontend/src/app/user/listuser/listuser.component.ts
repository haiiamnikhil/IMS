import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user/user.service';

@Component({
  selector: 'app-listuser',
  templateUrl: './listuser.component.html',
  styleUrls: ['./listuser.component.css']
})
export class ListuserComponent implements OnInit {

  users_list = []
  // test_data = [{'name':"Nikhil",'last_name':"Pradeep",'age':26},{'name':"asdsa",'last_name':"sad",'age':20}]
  test_data = ['nikhil','pradeep']
  name = "List User"
  constructor(private user: UserService) { }

  ngOnInit(){
    this.user.listUsers().subscribe(response => {
      if (response.success){
        this.users_list.push(response.data)
      } else {
        console.log('Something went wrong')
      }
    }, err => console.log(err));
  }

}

import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  header = new HttpHeaders({'Content-Type': 'application/json'})

  constructor(private http: HttpClient) { }
  

  userSignIn(credentials:any): Observable<any>{
    return this.http.post('/auth/signin/',credentials)
  }
}

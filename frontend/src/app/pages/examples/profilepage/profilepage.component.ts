import { Component, OnInit, OnDestroy } from "@angular/core";
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { data } from 'jquery';

@Component({
  selector: "app-profilepage",
  templateUrl: "profilepage.component.html"
})
export class ProfilepageComponent implements OnInit, OnDestroy {
  isCollapsed = true;
  focus;
  focus1;
  focus2;
  username;
  pass;
  constructor(private http: HttpClient, private router: Router) { }

  ngOnInit() {
    var body = document.getElementsByTagName("body")[0];
    body.classList.add("profile-page");
  }
  ngOnDestroy() {
    var body = document.getElementsByTagName("body")[0];
    body.classList.remove("profile-page");
  }
  submitu() {
    console.log(this.username, this.pass);
    var body = new FormData()
    body.append('username', this.username)
    body.append('password', this.pass)

    this.http.post<any>("http://127.0.0.1:8000/portal/api-token-auth/", body).subscribe(
      data => {
        console.log(data)
        localStorage.setItem('token', data["token"])
        this.router.navigateByUrl('/candidate')
      }
    )
  }
  submit() {
    console.log(this.username, this.pass);
    var body = new FormData()
    body.append('username', this.username)
    body.append('password', this.pass)

    this.http.post<any>("http://127.0.0.1:8000/portal/api-token-auth/", body).subscribe(
      data => {
        console.log(data)
        localStorage.setItem('hp_token', data["token"])
        this.router.navigateByUrl('/manager')
      }
    )
  }
}

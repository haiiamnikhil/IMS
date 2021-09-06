import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FirmProfileComponent } from './firm-profile.component';

describe('FirmProfileComponent', () => {
  let component: FirmProfileComponent;
  let fixture: ComponentFixture<FirmProfileComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FirmProfileComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FirmProfileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

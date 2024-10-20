class User:
    def introduce(user):
        print(f"반갑습니다. 저는 {user.name}입니다.")

user1 = User()
user2 = User()

user1.name = '해리문'
user2.name = '샐리권'

user1.email = 'aa@aa.com'
user2.email = 'bb@aa.com'


print(user2.email)
User.introduce(user1)
user1.introduce() #인스턴스가 메소드의 첫번째 argument(함수의 인자)로 자동으로 전달됨






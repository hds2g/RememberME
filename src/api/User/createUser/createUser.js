export default {
  Mutation: {
    createUser: async (_, args, { prisma }) => {
      console.log(args);
      const { username, email } = args;

      // check email already registered or not.
      const exist = await prisma.user.findOne({
        where: {
          email: email,
        },
      });

      if (exist) {
        throw Error("this email is already");
        console.log(exist);
        return false;
      }
      try {
        const user = await prisma.user.create({
          data: {
            username,
            email,
          },
        });
        return true;
      } catch {
        return false;
      }
    },
  },
};
